import torch as th
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pickle as pkl


class QlinearMixer(nn.Module):
    def __init__(self, args):
        super(QlinearMixer, self).__init__()

        self.name = 'qlinear'
        self.args = args
        self.n_agents = args.n_agents
        self.state_dim = int(np.prod(args.state_shape))
        self.unit_dim = args.unit_dim
        self.n_actions = args.n_actions
        self.sa_dim = self.state_dim + self.n_agents * self.n_actions

        self.embed_dim = args.mixing_embed_dim

        if getattr(args, "hypernet_layers", 1) == 1:
            self.weight_nn = nn.Linear(self.state_dim + self.unit_dim, 1, bias=False)  # weight
        elif getattr(args, "hypernet_layers", 1) == 2:
            hypernet_embed = self.args.hypernet_embed
            self.weight_nn = nn.Sequential(nn.Linear(self.state_dim + self.unit_dim, hypernet_embed),
                                           nn.ReLU(),
                                           nn.Linear(hypernet_embed, 1, bias=False))

        elif getattr(args, "hypernet_layers", 1) > 2:
            raise Exception("Sorry >2 embednet layers is not implemented!")
        else:
            raise Exception("Error setting number of embednet layers.")

        if self.args.state_bias:
            # V(s) instead of a bias for the last layers
            self.V = nn.Sequential(nn.Linear(self.state_dim, self.embed_dim),
                                   nn.ReLU(),
                                   nn.Linear(self.embed_dim, 1))

    def forward(self, agent_qs, states, actions):
        bs = agent_qs.size(0)
        states = states.reshape(-1, self.state_dim)
        unit_states = states[:, : self.unit_dim * self.n_agents]  # get agent own features from state
        unit_states = unit_states.reshape(-1, self.n_agents, self.unit_dim)
        unit_states = unit_states.permute(1, 0, 2)  # (agent_num, batch_size, unit_dim)

        agent_qs = agent_qs.view(-1, 1, self.n_agents)  # agent_qs: (batch_size, 1, agent_num)

        unit_states = th.cat((unit_states, states.reshape(1, -1, self.state_dim).repeat(self.n_agents, 1, 1)), dim=2)
        # unit_states: (agent_num, batch_size, state_dim + unit_dim)
        linear_weights = th.abs(self.weight_nn(unit_states))
        # linear_weights: (agent_num, batch_size, 1)

        # (batch_size, 1, agent_num) * (batch_size, 1, agent_num)
        linear_q = (agent_qs * linear_weights.permute(1, 2, 0)).sum(dim=2)

        if self.args.state_bias:
            # State-dependent bias
            v = self.V(states).view(-1, 1)  # v: (bs, 1)
            # head_qs: [head_num, bs, 1]
            y = linear_q + v  # y: (bs, 1)
        else:
            y = linear_q  # y: (bs, 1)
        # Reshape and return
        q_tot = y.view(bs, -1, 1)
        return q_tot
