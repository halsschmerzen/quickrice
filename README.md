# QuickRice

QuickRice is a simple and efficient command-line tool designed to help you manage and customize your desktop themes (rice) effortlessly. Whether you're looking to generate new themes, apply existing ones, or simply list all available options, QuickRice provides an intuitive interface to streamline your desktop customization experience.

## Features

- **Generate New Themes:** Create personalized desktop themes tailored to your preferences.
- **Apply Existing Themes:** Easily switch between your saved themes with a single command.
- **List Available Themes:** View all the themes you have created and stored.
- **Interactive Menu:** Navigate through options using an easy-to-use interactive interface.
- **Automated Package Management:** Ensures all necessary packages are installed and up-to-date.

## Installation

### Prerequisites

- **Python 3.6+**: Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).

### Using `install.sh`

It is recommended to use the given install.sh file. As of November 2024 the AUR and pip is not maintained. 

Make sure the installation script is executable:

   ```bash
   chmod +x install.sh 
   ```


For a local installation (recommended) use:

   ```bash
   ./install.sh install --local
   ```

For a global installation use:

   ```bash
   ./install.sh install --global
   ```


## Usage

After installation, you can use QuickRice via the terminal.

### Command-Line Interface

- **Generate a New Theme**

  ```bash
  quickrice generate
  ```

  Follow the prompts to create a new desktop theme.

- **Apply an Existing Theme**

  ```bash
  quickrice apply <theme_name>
  ```

  Replace `<theme_name>` with the name of the theme you wish to apply.

- **List Available Themes**

  ```bash
  quickrice list
  ```

  Displays all the themes you have created.

### Interactive Menu

Launch the interactive menu by simply running:

```bash
quickrice
```

Navigate through the options to generate, apply, or manage your themes with ease.

## Contributing

Contributions are welcome! If you'd like to contribute to QuickRice, please follow these steps:

1. **Fork the Repository**

   Click the "Fork" button on the top-right corner of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/halsschmerzen/quickrice.git
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Your Changes**

5. **Commit Your Changes**

   ```bash
   git commit -m "Add your message here"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Open a Pull Request**

   Navigate to the original repository and open a pull request with your changes.

## License

This project is licensed under the MIT License.

## Support

If you encounter any issues or have questions, feel free to open an [issue](https://github.com/halsschmerzen/quickrice/issues) on GitHub.

## Acknowledgements

- Inspired by various desktop customization tools.
- Thanks to the open-source community for their invaluable resources and support.
