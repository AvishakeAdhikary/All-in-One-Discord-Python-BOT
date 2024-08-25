def update_env_file(env_file_path, key, value):
    # Read the existing content of the .env file
    lines = []
    try:
        with open(env_file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("'.env' file not found.")

    # Update or add the key-value pair
    key_exists = False
    with open(env_file_path, 'w') as file:
        for line in lines:
            if line.startswith(f'{key}='):
                file.write(f'{key}={value}\n')
                key_exists = True
            else:
                file.write(line)
        
        if not key_exists:
            file.write(f'{key}={value}\n')