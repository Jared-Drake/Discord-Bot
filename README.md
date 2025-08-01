# Cult Bot - Discord Minecraft Server Management Bot

A comprehensive Discord bot designed for Minecraft server communities. This bot provides application management, automated role assignment, server information posting, and community management features.

## 🚀 Features

### Core Functionality
- **Application System**: Comprehensive application process with customizable questions
- **Role Management**: Automatic role assignment for new members and application status
- **Server Information**: Automated posting of rules, FAQ, and join instructions
- **Admin Tools**: Review applications, manage server content, and monitor activity
- **Database Storage**: SQLite database for persistent application storage

### Commands
- **User Commands**: `!apply`, `!bothelp`
- **Admin Commands**: `!applications`, `!postrules`, `!postfaq`, `!postjoininfo`

## 📋 Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher
- Discord server with administrator permissions
- Discord Developer Account

### 2. Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd discord-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Discord Bot Setup

1. **Create Discord Application**:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and name it
   - Go to "Bot" section and click "Add Bot"
   - Copy the bot token

2. **Configure Bot Permissions**:
   - Under "Privileged Gateway Intents", enable:
     - Message Content Intent
     - Server Members Intent

3. **Invite Bot to Server**:
   - Go to "OAuth2" → "URL Generator"
   - Select scopes: `bot` and `applications.commands`
   - Select permissions:
     - Send Messages
     - Embed Links
     - Manage Roles
     - Read Message History
     - Use Slash Commands
   - Copy the generated URL and authorize the bot

### 4. Configuration

1. **Set up your bot token**:
   ```bash
   # Create token.txt file
   echo "your_bot_token_here" > token.txt
   ```

2. **Configure server settings**:
   ```bash
   # Copy the example config
   cp config.example.json config.json
   ```
   
   Then edit `config.json` with your server's channel and role IDs:
   ```json
   {
     "application_questions": [
       "What is your Minecraft username?",
       "How old are you?",
       "How long have you been playing Minecraft?",
       "What type of player are you? (Builder, Redstone, PvP, etc.)",
       "Why do you want to join our server?",
       "Do you have any experience with other Minecraft servers?",
       "How much time do you plan to spend on the server?",
       "Do you agree to follow our server rules? (Yes/No)",
       "Any additional information you'd like to share?"
     ],
     "application_channel_id": 1234567890123456789,
     "admin_role_id": 1234567890123456789,
     "log_channel_id": 1234567890123456789,
     "approved_role_id": 1234567890123456789,
     "denied_role_id": 1234567890123456789,
     "applicant_role_id": 1234567890123456789,
     "rules_channel_id": 1234567890123456789,
     "faq_channel_id": 1234567890123456789,
     "join_channel_id": 1234567890123456789
   }
   ```

3. **Get Channel/Role IDs**:
   - Enable Developer Mode in Discord (User Settings → Advanced → Developer Mode)
   - Right-click on channels/roles and select "Copy ID"

### 5. Run the Bot

```bash
python bot.py
```

## 🎮 Usage

### User Commands
- `!apply` - Start the application process
- `!bothelp` - Show help information

### Admin Commands
- `!applications` - List pending applications
- `!postrules` - Post server rules in rules channel
- `!postfaq` - Post FAQ in FAQ channel
- `!postjoininfo` - Post join instructions in join channel

## 📁 Project Structure

```
├── bot.py                    # Main bot entry point
├── config.json               # Server configuration
├── config.example.json       # Configuration template
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── .gitignore               # Git ignore rules
├── cogs/                    # Bot command modules
│   ├── applications.py      # Application system
│   ├── admin.py            # Admin commands
│   ├── rules.py            # Rules posting
│   ├── faq.py              # FAQ posting
│   └── join_info.py        # Join instructions
├── events/                  # Event handlers
│   └── member_events.py    # Member join events
└── utils/                   # Utility functions
    └── database.py         # Database operations
```

## 🔧 Configuration

### Channel IDs Required
- `application_channel_id`: Channel where users can apply
- `log_channel_id`: Channel for application notifications
- `rules_channel_id`: Channel for server rules
- `faq_channel_id`: Channel for FAQ
- `join_channel_id`: Channel for join instructions

### Role IDs Required
- `admin_role_id`: Role that can review applications
- `approved_role_id`: Role given to approved users
- `denied_role_id`: Role given to denied users
- `applicant_role_id`: Role given to new members

### Customizing Application Questions
Edit the `application_questions` array in `config.json` to customize the application process.

## 🛡️ Security Features

- **Token Protection**: Bot token stored in separate file (not in Git)
- **Admin-Only Commands**: Sensitive commands restricted to administrators
- **Input Validation**: All user inputs are validated
- **Error Handling**: Comprehensive error handling and logging

## 🐛 Troubleshooting

### Common Issues

1. **Bot not responding**:
   - Check if bot token is correct
   - Verify bot has proper permissions
   - Ensure bot is online

2. **Commands not working**:
   - Check bot permissions in Discord
   - Verify channel/role IDs are correct
   - Check console for error messages

3. **Role assignment issues**:
   - Ensure bot has "Manage Roles" permission
   - Check role hierarchy (bot role must be above managed roles)
   - Verify role IDs are correct

### Getting Help

1. Check the bot's console output for error messages
2. Verify all required permissions are granted
3. Ensure channel and role IDs are correct
4. Make sure the bot is connected to your server

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Note**: Make sure to keep your `token.txt` file secure and never commit it to version control. The `.gitignore` file is configured to prevent accidental commits of sensitive files. 