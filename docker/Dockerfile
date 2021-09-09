FROM pymarl:1.0
MAINTAINER dong

## -- SMAC
RUN pip3 uninstall smac -y

RUN pip3 install git+https://github.com/oxwhirl/smac.git

ENV SC2PATH /Qatten/3rdparty/StarCraftII

WORKDIR /Qatten

COPY multiagentenv.py /usr/local/lib/python3.5/dist-packages/smac/env/
