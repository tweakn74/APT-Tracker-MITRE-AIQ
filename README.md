# APT Tracker - MITRE ATT&CK & AttackIQ Integration

A dynamic threat intelligence dashboard for cybersecurity professionals to analyze and emulate Advanced Persistent Threat (APT) groups.

🌐 **Live Demo**: [https://tweakn74.github.io/APT-Tracker-MITRE-AIQ/](https://tweakn74.github.io/APT-Tracker-MITRE-AIQ/)

## 🎯 Features

- **APT Group Profiles**: Detailed information on major threat actors (FIN7, APT29, Lazarus, APT28, APT41, Wizard Spider)
- **MITRE ATT&CK Integration**: Maps attack techniques to specific threat groups
- **AttackIQ Integration**: Provides testable security scenarios for each APT group
- **Interactive Filtering**: Filter by APT group, target industry, and attack type
- **Attack Chain Visualization**: Visual representation of attack progression
- **Multi-dimensional Analysis**: Shows MITRE techniques, attack steps, search terms, and AttackIQ scenarios

## 🚀 Quick Start

### Local Development

1. **Clone the repository**:

   ```bash
   git clone https://github.com/<username>/APT-Tracker-MITRE-AIQ.git
   cd APT-Tracker-MITRE-AIQ
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Run local development server**:

   ```bash
   npm run dev
   ```

   Open [http://localhost:5500](http://localhost:5500) in your browser.

### Testing

Run Playwright tests to verify functionality:

```bash
npm test
```

Run tests with UI mode for debugging:

```bash
npm run test:ui
```

## 🏗️ Architecture

- **Frontend**: Vanilla HTML/CSS/JavaScript (no build step required)
- **Data**: Embedded JSON database with APT group intelligence
- **Testing**: Playwright for end-to-end testing
- **CI/CD**: GitHub Actions for automated testing and deployment
- **Hosting**: GitHub Pages

## 📊 Data Sources

- MITRE ATT&CK Framework
- Government cybersecurity advisories
- Security vendor threat intelligence reports
- AttackIQ security testing scenarios

## 🎯 Target Audience

- Cybersecurity professionals
- Threat hunters
- Security teams
- Red team operators
- Security researchers

## 📚 Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [Data Model](docs/DATA_MODEL.json)
- [Contributing Guidelines](docs/CONTRIBUTING.md)

## 🤝 Contributing

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Live Demo

Visit the live dashboard: [https://<username>.github.io/APT-Tracker-MITRE-AIQ/](https://<username>.github.io/APT-Tracker-MITRE-AIQ/)
