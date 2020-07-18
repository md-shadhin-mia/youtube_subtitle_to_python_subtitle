FROM gitpod/workspace-full

USER gitpod

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
 RUN sudo apt-get -q update && \
     sudo apt-get install -yq bastet \
     p7zip-full \
#
# More information: https://www.gitpod.io/docs/config-docker/
