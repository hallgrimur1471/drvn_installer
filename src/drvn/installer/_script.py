import logging
import argparse

import drvn.installer.example_module
import drvn.installer.installer as installer
import drvn.installer._logging as drvn_logger


def main():
    args = _parse_arguments()

    if args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    drvn_logger.configure(log_level)

    if args.list_installable_software:
        for software in installer.get_installable_software():
            print(software)
        return

    if args.install:
        software_to_install = args.install.split(",")
        for software in software_to_install:
            installer.install(software, args.with_drvn_configs)

    logging.info(drvn.installer.example_module.example_public_function())


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = (
        "Installers for various software with options "
        + "on additionally installing custom configs."
    )
    parser.add_argument(
        "-i",
        "--install",
        metavar="SOFTWARE_LIST",
        help="Comma seperated list of software to install. "
        + "Example: vim,tmux",
    )
    parser.add_argument(
        "-c",
        "--with-drvn-configs",
        action="store_true",
        help="Additionally install drvn's custom configs with the software "
        + "(drvn's .vimrc with vim, etc)",
    )
    parser.add_argument(
        "-l",
        "--list-installable-software",
        action="store_true",
        help="Output a list of all software that this installer can install",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enables printing of debug statements",
    )
    arguments = parser.parse_args()
    return arguments
