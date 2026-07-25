# Day 43 - Linux Basics and Shell Scripting

## Essential Navigation Commands
```bash
pwd           # print working directory - shows where you are
ls            # list files in current directory
ls -la        # list all files including hidden, with permissions
cd learning   # change into learning directory
cd ..         # go up one directory
cd ~          # go to home directory
mkdir learning # create a new directory
touch hello.py # create an empty file
```

## File Operations
```bash
cat hello.py              # read and display file contents
cp hello.py backup.py     # copy a file
mv backup.py learning/    # move a file to another directory
rm hello.py               # delete a file
grep "Hello" hello.py     # search for text inside a file
echo "text" > file.py     # write text to a file (overwrites)
echo "text" >> file.py    # append text to a file
```

## File Permissions
Format: -rwxr-xr-x

r = read = 4
w = write = 2
x = execute = 1

Common permissions:
- 755 = rwxr-xr-x (owner full, others read+execute) - scripts
- 644 = rw-r--r-- (owner read+write, others read only) - files
- 777 = rwxrwxrwx (everyone full access) - avoid in production

```bash
chmod 755 script.sh   # change permissions using numbers
chmod +x script.sh    # add execute permission
```

## Shell Scripting

### Basic script structure
```bash
#!/bin/bash
# This is a comment
echo "Hello from shell script"
```

### Variables
```bash
APP_NAME="Django Contact Book"
echo "Deploying $APP_NAME..."
```

### Conditionals
```bash
if [ "$ENVIRONMENT" == "production" ]; then
    echo "Running production checks..."
fi
```

### Error handling
```bash
pip install -r requirements.txt 2>/dev/null || echo "No requirements.txt found"
# 2>/dev/null suppresses error output
# || runs fallback command if first command fails
```

### Making script executable and running
```bash
chmod +x deploy.sh
./deploy.sh
```

## Real Deployment Script Structure
```bash
#!/bin/bash
APP_NAME="My App"
ENVIRONMENT="production"

echo "Deploying $APP_NAME to $ENVIRONMENT..."

if [ "$ENVIRONMENT" == "production" ]; then
    echo "Backing up database..."
    # pg_dump command here
fi

git pull origin main
pip install -r requirements.txt
python manage.py migrate
systemctl restart gunicorn

echo "Deployment complete!"
```

## Key Concepts
- Every Linux command is a program that lives in /usr/bin or /bin
- Everything in Linux is a file - even directories and devices
- Hidden files start with . (dot)
- Shell scripts automate repetitive tasks
- Always use chmod +x before running a script
- #!/bin/bash tells the OS which interpreter to use
