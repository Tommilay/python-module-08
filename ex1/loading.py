#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: tny-onin <tny-onin@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/05 14:13:17 by tny-onin            #+#    #+#            #
#   Updated: 2026/07/07 16:53:22 by tny-onin           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from importlib import import_module, metadata


def main() -> None:
    modules = [
        "pandas",
        "numpy",
        "matplotlib",
        "requests"
    ]
    print("\n\
LOADING STATUS: Loading programs ...\n")
    try:
        for module in modules:
            import_module(module)
            print(f"[OK] {module} ({metadata.version(module)})")
    except Exception:
        print(f"[MISSING] {module}")
    print()
    try:
        import numpy as np
        data = np.random.normal(
            loc=50,
            scale=15,
            size=1000
        )
        print("Analyzing Matrix data ...")

        import pandas as pd
        print("Processing 1000 data points ...")
        df = pd.DataFrame({
                "signal": data
            })

        import matplotlib.pyplot as plt
        print("Generating visualization ...")
        plt.hist(df["signal"])
        plt.title("Matrix data")
        plt.savefig("matrix_analisys.png")
    except Exception as e:
        print(e)

    print()
    print("Analysis complete!")
    print("Results saved: matrix_analisys.png")


if __name__ == "__main__":
    main()
