#!/usr/bin/env bash

# taken from https://docs.modular.com/mojo/manual/get-started

python3 -m venv mojo-venv && source mojo-venv/bin/activate

modular install mojo

MOJO_PATH=$(modular config mojo.path) \
  && BASHRC=$( [ -f "$HOME/.bash_profile" ] && echo "$HOME/.bash_profile" || echo "$HOME/.bashrc" ) \
  && echo 'export MODULAR_HOME="'$HOME'/.modular"' >> "$BASHRC" \
  && echo 'export PATH="'$MOJO_PATH'/bin:$PATH"' >> "$BASHRC" \
  && source "$BASHRC"
