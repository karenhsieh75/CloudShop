# run.sh
#!/bin/bash

# Ensure the data directory exists
mkdir -p data

# Set database path
DB_PATH="data/cloudshop.db"

# If user passes the --reset parameter, delete the database
if [ "$1" == "--reset" ]; then
   if [ -f "$DB_PATH" ]; then
       echo "Resetting database..."
       rm "$DB_PATH"
   fi
fi

echo "Running CloudShop CLI..."

# Execute the CLI application
python3 main.py