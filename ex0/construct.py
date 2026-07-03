import sys
import site

def is_insystem() -> bool:
    return sys.prefix == sys.base_prefix

def print_construct(
        status: str,
        current_path: str,
        venv: str,
        env_path: str
        ):
    print(f"\nMATRIX STATUS:{status}\n")
    print(f"Current Python: {current_path}")
    print(f"Virtual Environment: {venv}")
    print(f"{env_path}\n")

def main() -> None:
    current_path = sys.executable
    if is_insystem():
        status = "You're in the global environment!"
        env_name = "None detected"
        path_env_ = "\nWARNING: you're in the the globale environment!\
The machines can see everything you install"
    
        print_construct(status, current_path, env_name, path_env_)

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # on Unix")
        print("matrix_env\\Scripts\\activate #on windows")
        print()
        print("Then run this program again.")
    else:
        status = "Welcom to the construct"
        path_env = sys.prefix
        env_name = path_env.split("\\")
        env_name = env_name[len(env_name) - 1]
        path_env_ = f"Environment path: {path_env}"

        print_construct(status, current_path, env_name, path_env_)

        print("SUCCESS: you're in isolated environment!")
        print("Safe to install package without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        for path in site.getsitepackages():
            print(path if "site" in path else "", end="")



if __name__ == "__main__":
    main()