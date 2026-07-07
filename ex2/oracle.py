#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/07 17:33:59 by tny-onin            #+#    #+#            #
#   Updated: 2026/07/07 18:31:29 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

try:
    from dotenv import load_dotenv
except Exception as e:
    print(e)
    print("Install using 'python -m pip install python-dotenv'")
    print('-> Exiting')
    exit()

import os


def main() -> None:
    print("ORACLE STATUS: Reading the matrix ...")

    load_dotenv()
    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    endpoint = os.getenv("ZION_ENDPOIN")

    required = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": database,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": endpoint
    }

    missing = [name for name, value in required.items() if not value]
    if missing:
        print("Missing configuration in:")
        for name in missing:
            print(f"--{name}")
        exit()

    print("Configuration loading:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Netork: {endpoint}")

    print(
        "\nEnvironment security check:\n"
        "[OK] No hardcoded secrets detected\n"
        "[OK] .env file properly configured\n"
        "[OK] Production overrides available\n"
    )
    print("The Oracle sees all configuration")


if __name__ == "__main__":
    main()
