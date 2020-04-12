import logging


def install(software, with_drvn_configs):
    if software not in get_installable_software():
        raise RuntimeError(
            f"Installing '{software}' is not supported by this installer."
        )

    install_function = _get_install_function(software)
    install_function(with_drvn_configs)


def get_installable_software():
    installable_software = [
        software
        for software, install_function in _SOFTWARE_TO_INSTALL_FUNCTION.items()
    ]
    return installable_software


def _get_install_function(software):
    return _SOFTWARE_TO_INSTALL_FUNCTION[software]


def _install_vim(with_drvn_configs):
    logging.debug("Installing vim ...")


def _install_tmux(with_drvn_configs):
    logging.debug("Installing tmux ...")


_SOFTWARE_TO_INSTALL_FUNCTION = {"vim": _install_vim, "tmux": _install_tmux}
