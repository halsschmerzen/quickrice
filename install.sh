#!/bin/bash

# install.sh - Installation and Uninstallation Script for QuickRice
# Usage:
#   ./install.sh install --global   # Install QuickRice globally
#   ./install.sh install --local    # Install QuickRice locally
#   ./install.sh uninstall --global  # Uninstall QuickRice from global installation
#   ./install.sh uninstall --local   # Uninstall QuickRice from local installation

# Function to display usage information
usage() {
    echo "Usage:"
    echo "  $0 install [--global|--local]   # Install QuickRice globally or locally"
    echo "  $0 uninstall [--global|--local] # Uninstall QuickRice from global or local installation"
    echo "  $0 help                         # Display this help message"
    exit 1
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install QuickRice
install_quickrice() {
    INSTALL_TYPE=$1

    if [ "$INSTALL_TYPE" == "--global" ]; then
        INSTALL_DIR="/opt/quickrice"
        SYMLINK_DIR="/usr/local/bin"
        SYMLINK_PATH="$SYMLINK_DIR/quickrice"
        NEED_SUDO=true

        # Check if the user has sudo privileges
        if ! sudo -v >/dev/null 2>&1; then
            echo "Error: Global installation requires sudo privileges."
            exit 1
        fi
    elif [ "$INSTALL_TYPE" == "--local" ]; then
        INSTALL_DIR="$HOME/.quickrice"
        SYMLINK_DIR="$HOME/.local/bin"
        SYMLINK_PATH="$SYMLINK_DIR/quickrice"
        NEED_SUDO=false
    else
        echo "Error: Please specify --global or --local for installation."
        usage
    fi

    # Check if installation directory already exists
    if [ -d "$INSTALL_DIR" ]; then
        echo "QuickRice is already installed in $INSTALL_DIR."
        exit 1
    fi

    # Create the installation directory
    echo "Creating installation directory at $INSTALL_DIR..."
    if [ "$NEED_SUDO" = true ]; then
        sudo mkdir -p "$INSTALL_DIR"
    else
        mkdir -p "$INSTALL_DIR"
    fi

    # Copy all project files to the installation directory
    echo "Copying project files to $INSTALL_DIR..."
    if [ "$NEED_SUDO" = true ]; then
        sudo cp -r quickrice/* "$INSTALL_DIR/"
    else
        cp -r quickrice/* "$INSTALL_DIR/"
    fi

    # Ensure the main.py script is executable
    echo "Setting executable permissions for main.py..."
    if [ "$NEED_SUDO" = true ]; then
        sudo chmod +x "$INSTALL_DIR/main.py"
    else
        chmod +x "$INSTALL_DIR/main.py"
    fi

    # Create the symlink
    echo "Creating symlink at $SYMLINK_PATH -> $INSTALL_DIR/main.py..."
    if [ -L "$SYMLINK_PATH" ]; then
        echo "Symlink $SYMLINK_PATH already exists. Removing it..."
        if [ "$NEED_SUDO" = true ]; then
            sudo rm "$SYMLINK_PATH"
        else
            rm "$SYMLINK_PATH"
        fi
    fi

    if [ "$INSTALL_TYPE" == "--global" ]; then
        sudo ln -s "$INSTALL_DIR/main.py" "$SYMLINK_PATH"
    else
        # Create ~/.local/bin if it doesn't exist
        mkdir -p "$SYMLINK_DIR"

        # Check if ~/.local/bin is in PATH
        if [[ ":$PATH:" != *":$SYMLINK_DIR:"* ]]; then
            echo "Adding $SYMLINK_DIR to PATH in ~/.bashrc..."
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
            echo "Please reload your shell or run 'source ~/.bashrc' to apply the changes."
        fi

        ln -s "$INSTALL_DIR/main.py" "$SYMLINK_PATH"
    fi

    echo "QuickRice has been successfully installed."
}

# Function to uninstall QuickRice
uninstall_quickrice() {
    INSTALL_TYPE=$1

    if [ "$INSTALL_TYPE" == "--global" ]; then
        INSTALL_DIR="/opt/quickrice"
        SYMLINK_DIR="/usr/local/bin"
        SYMLINK_PATH="$SYMLINK_DIR/quickrice"
        NEED_SUDO=true
    elif [ "$INSTALL_TYPE" == "--local" ]; then
        INSTALL_DIR="$HOME/.quickrice"
        SYMLINK_DIR="$HOME/.local/bin"
        SYMLINK_PATH="$SYMLINK_DIR/quickrice"
        NEED_SUDO=false
    else
        echo "Error: Please specify --global or --local for uninstallation."
        usage
    fi

    # Check if installation directory exists
    if [ ! -d "$INSTALL_DIR" ]; then
        echo "QuickRice is not installed in $INSTALL_DIR."
        exit 1
    fi

    # Remove the symlink
    if [ -L "$SYMLINK_PATH" ]; then
        echo "Removing symlink at $SYMLINK_PATH..."
        if [ "$INSTALL_TYPE" == "--global" ]; then
            if [ "$(id -u)" -ne 0 ]; then
                sudo rm "$SYMLINK_PATH"
            else
                rm "$SYMLINK_PATH"
            fi
        else
            rm "$SYMLINK_PATH"
        fi
    else
        echo "Symlink $SYMLINK_PATH does not exist."
    fi

    # Remove the installation directory
    echo "Removing installation directory at $INSTALL_DIR..."
    rm -rf "$INSTALL_DIR"

    echo "QuickRice has been successfully uninstalled."
}

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
    usage
fi

# Parse the first argument
ACTION=$1

case "$ACTION" in
    install)
        if [ $# -ne 2 ]; then
            echo "Error: Missing option for install."
            usage
        fi
        OPTION=$2
        install_quickrice "$OPTION"
        ;;
    uninstall)
        if [ $# -ne 2 ]; then
            echo "Error: Missing option for uninstall."
            usage
        fi
        OPTION=$2
        uninstall_quickrice "$OPTION"
        ;;
    help)
        usage
        ;;
    *)
        echo "Error: Unknown action '$ACTION'."
        usage
        ;;
esac