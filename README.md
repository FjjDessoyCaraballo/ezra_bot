# Ezra - Web Archive Preservation Tool

![Ezra Preview](/ezra_preview.png)

A dedicated web scraping and archival tool designed to preserve knowledge from the inactive [BRL Center website](https://web.archive.org/web/20240222194932/http://brlcenter.org/) by systematically retrieving and downloading `.zip` files through the Internet Archive's Wayback Machine.

## Purpose

Ezra serves as a digital preservation tool, ensuring that valuable educational and research materials from the now-defunct BRL Center remain accessible. The tool operates with respect for the Internet Archive's resources by implementing intelligent caching and rate limiting.

## Features

### Core Functionality
- **Intelligent Web Scraping**: Parses archived HTML content to extract downloadable file links
- **Selective File Filtering**: Automatically identifies and processes only `.zip` files
- **Local Database Caching**: Uses SQLite to store discovered links, preventing redundant requests
- **Progress Tracking**: Real-time download progress with file size reporting
- **Integrity Verification**: Validates downloaded files against expected sizes
- **Resume Capability**: Skips already downloaded files automatically

### User Experience
- **Intuitive GUI**: Clean Tkinter-based interface with clear action buttons
- **Real-time Output**: Live logging and progress updates in the interface
- **Error Handling**: Comprehensive error reporting and logging
- **Resource Respectful**: Built-in delays and rate limiting to respect server resources

### Technical Features
- **Zero External Dependencies**: Uses only Python standard library
- **Cross-platform**: Compatible with Windows, macOS, and Linux
- **Robust Error Recovery**: Handles network issues and file corruption gracefully
- **Comprehensive Logging**: Detailed logs saved to `ezra.log` for debugging

## Installation

### Prerequisites

- **Python 3.12.3** or higher
- **Tkinter** (usually included with Python, but may need separate installation on some Linux distributions)

### Verify Python Version

```bash
python3 --version
```

### Linux (Ubuntu/Debian) - Install Tkinter if needed

```bash
sudo apt update
sudo apt install python3-tk
```

### Getting Started

1. **Clone or download** the repository
2. **Navigate** to the project directory
3. **Run the application**:

```bash
python3 ezra.py
```

**Alternative**: Use the provided `run_ezra` executable:
```bash
./run_ezra
```

## Usage Guide

### Application Workflow

Ezra operates in two distinct phases:

#### 1. **Scraping Phase**
- Click **"Scrape"** to begin HTML parsing
- Connects to the archived BRL Center website
- Extracts all `.zip` file links from the page
- Stores discovered links in local SQLite database
- Displays progress and found links in real-time

#### 2. **Download Phase**
- Click **"Download"** to begin file retrieval
- Processes all discovered `.zip` files from the database
- Downloads files to the `downloads/` directory
- Shows download progress, file sizes, and completion status
- Automatically skips already downloaded files

### Interface Overview

```
┌─────────────────┬─────────────────────────────────────┐
│   Give Ezra     │             Output                  │
│   purpose       │                                     │
│                 │  Real-time logs and progress        │
│   [Scrape]      │  updates appear here...             │
│   [Download]    │                                     │
│   [Close]       │                                     │
└─────────────────┴─────────────────────────────────────┘
```

## Technical Architecture

### File Structure

```
ezra/
├── ezra.py              # Main application
├── run_ezra             # Executable launcher
├── README.md            # Documentation
├── LICENSE             # MIT License
├── .gitignore          # Git ignore rules
├── ezra.log            # Application logs (generated)
├── brlcenter.db        # SQLite database (generated)
├── downloads/          # Downloaded files (generated)
└── ezra_preview.png    # GUI preview image
```

### Core Components

#### **Communion Class** (HTMLParser)
Custom HTML parser that inherits from `html.parser.HTMLParser`:
- Extracts `href` attributes from anchor tags
- Filters for downloadable content links
- Returns list of discovered URLs

#### **Database Functions**
- `theoxenia()`: Initializes SQLite database and table structure
- `via_dolorosa()`: Inserts discovered links with duplicate prevention
- `first_day()`: Retrieves and filters stored links for `.zip` files

#### **Download Engine**
- `second_day()`: Handles individual file downloads with progress tracking
- `ascension()`: Orchestrates the complete download process
- Built-in retry logic and integrity verification

#### **GUI Framework**
- Tkinter-based interface with responsive layout
- Real-time output display with scrolling
- Thread-safe GUI updates during operations

### Database Schema

```sql
CREATE TABLE brl_links (
    id INTEGER PRIMARY KEY,
    link TEXT UNIQUE,
    available TEXT,
    last_fetch TEXT
);
```

## ⚠️ Important Constraints

### Operational Limitations
- **No Interruption**: Ezra cannot be safely closed during active downloads
- **Sequential Processing**: Downloads are processed one at a time to respect server limits
- **Network Dependent**: Requires stable internet connection for optimal performance

### Resource Considerations
- **Storage Space**: Ensure adequate disk space for downloaded archives
- **Download Time**: Large files may take considerable time depending on connection speed
- **Rate Limiting**: Built-in 15-second delays between downloads to respect Internet Archive

## 🐛 Troubleshooting

### Common Issues

#### **"Module 'tkinter' not found"**
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# CentOS/RHEL
sudo yum install tkinter
# or
sudo dnf install python3-tkinter
```

#### **Downloads Failing**
- Check internet connection stability
- Verify the Internet Archive is accessible
- Review `ezra.log` for detailed error information

#### **GUI Not Responding**
- This is normal during download operations
- Do NOT force-close the application
- Wait for current operation to complete

#### **Database Errors**
- Ensure write permissions in the application directory
- Delete `brlcenter.db` to reset (will require re-scraping)

## 📊 Performance Expectations

### Typical Metrics
- **Scraping Phase**: 30-60 seconds depending on archive response time
- **Download Speed**: Limited by Internet Archive bandwidth and your connection
- **File Sizes**: Range from several MB to multiple GB per archive
- **Total Download Time**: Can range from hours to days for complete collection

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Test thoroughly with both scraping and download functionality
4. Submit pull request with detailed description

### Code Style
- Follow existing naming conventions (including the biblical function names)
- Maintain comprehensive error handling
- Add logging for new features
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
Copyright (c) 2025 Felipe Justo José Dessoy Caraballo
```

## Acknowledgments

- **Internet Archive**: For providing the Wayback Machine service
- **BRL Center**: For the original educational content being preserved
- **Python Community**: For the excellent standard library that makes this possible

## ⚡ Quick Start

```bash
# 1. Verify Python version
python3 --version

# 2. Run Ezra
python3 ezra.py

# 3. Click "Scrape" to discover files
# 4. Click "Download" to retrieve archives
# 5. Wait patiently for completion
# 6. Find your files in the downloads/ directory
```

---

**Remember**: Ezra is a preservation tool designed to rescue knowledge from digital oblivion. Use it responsibly and with respect for the resources it accesses.
