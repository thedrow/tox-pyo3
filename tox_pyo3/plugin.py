# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import pluggy

hookimpl = pluggy.HookimplMarker("tox")

log = logging.getLogger('pyo3')


@hookimpl
def tox_testenv_create(venv, action):
    venv.envconfig.whitelist_externals.append('pyo3-pack')


@hookimpl
def tox_testenv_install_deps(venv, action):
    basepath = venv.envconfig.changedir
    if not Path(basepath, 'Cargo.toml').exists():
        log.info("No Rust extension found. Skipping...")
        return
    cmd = venv.getcommandpath("pyo3-pack")
    action.setactivity("pyo3", "Building Rust extension module")
    venv._pcall([cmd, "develop"],
                venv=True,
                action=action,
                cwd=basepath,
                redirect=True,
                returnout=True)
