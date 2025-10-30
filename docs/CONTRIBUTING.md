# Contributing to APT Tracker

Thank you for your interest in contributing to the APT Tracker project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** first to avoid duplicates
2. **Use the issue template** when creating new issues
3. **Provide detailed information**:
   - Steps to reproduce
   - Expected vs actual behavior
   - Browser and OS information
   - Screenshots if applicable

### Suggesting Enhancements

1. **Check the roadmap** in the README
2. **Open a feature request** with detailed description
3. **Explain the use case** and benefits
4. **Consider implementation complexity**

### Contributing Code

#### Prerequisites

- Node.js 20 or higher
- Git
- Basic knowledge of HTML/CSS/JavaScript
- Familiarity with Playwright testing

#### Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/APT-Tracker-MITRE-AIQ.git
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

4. **Run tests**:
   ```bash
   npm test
   ```

#### Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow the coding standards below
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**:
   ```bash
   npm test
   ```

4. **Commit your changes**:
   ```bash
   git commit -m "feat: add new APT group analysis feature"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   - Use the PR template
   - Link related issues
   - Provide clear description of changes

## 📋 Coding Standards

### HTML
- Use semantic HTML5 elements
- Include proper ARIA labels for accessibility
- Validate markup with W3C validator

### CSS
- Use CSS custom properties for theming
- Follow BEM naming convention for classes
- Ensure responsive design (mobile-first)
- Test across major browsers

### JavaScript
- Use modern ES6+ syntax
- Follow functional programming principles
- Add JSDoc comments for functions
- Handle errors gracefully
- Avoid global variables

### Data Contributions

#### Adding New APT Groups

1. **Research thoroughly** using credible sources:
   - Government advisories
   - Security vendor reports
   - MITRE ATT&CK documentation
   - Academic research

2. **Follow the data schema** in `docs/DATA_MODEL.json`

3. **Include all required fields**:
   - Name and aliases
   - Origin and first seen date
   - Target industries and regions
   - MITRE ATT&CK techniques
   - Attack chain phases
   - Search terms for threat hunting

4. **Verify MITRE technique IDs** are current and accurate

5. **Add AttackIQ scenarios** if available

#### Data Quality Standards

- **Accuracy**: All information must be verifiable
- **Completeness**: Include all available relevant data
- **Consistency**: Follow existing naming conventions
- **Timeliness**: Use the most recent information available

### Testing Requirements

#### Required Tests for New Features

1. **Smoke tests**: Basic functionality works
2. **Schema validation**: Data conforms to JSON schema
3. **Integration tests**: Components work together
4. **Accessibility tests**: WCAG compliance
5. **Mobile tests**: Responsive design works

#### Test Writing Guidelines

- Use descriptive test names
- Test both positive and negative cases
- Include edge cases
- Mock external dependencies
- Keep tests independent and isolated

## 🔍 Code Review Process

### Review Criteria

1. **Functionality**: Does the code work as intended?
2. **Quality**: Is the code clean and maintainable?
3. **Testing**: Are there adequate tests?
4. **Documentation**: Is the code well-documented?
5. **Security**: Are there any security concerns?
6. **Performance**: Does it impact application performance?

### Review Timeline

- Initial review within 48 hours
- Follow-up reviews within 24 hours
- Approval requires at least one maintainer review

## 📚 Resources

### Documentation
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [AttackIQ Platform](https://www.attackiq.com/)
- [Playwright Testing](https://playwright.dev/)

### Threat Intelligence Sources
- [CISA Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories)
- [FBI IC3 Reports](https://www.ic3.gov/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

### Development Tools
- [VS Code](https://code.visualstudio.com/)
- [GitHub CLI](https://cli.github.com/)
- [Node.js](https://nodejs.org/)

## 🏷️ Commit Message Convention

Use conventional commits format:

```
type(scope): description

[optional body]

[optional footer]
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```
feat(apt-data): add APT41 group profile
fix(filtering): resolve industry filter bug
docs(readme): update installation instructions
test(schema): add validation for new fields
```

## 🎯 Getting Help

- **Discord**: Join our community server
- **Issues**: Use GitHub issues for bugs and features
- **Discussions**: Use GitHub discussions for questions
- **Email**: Contact maintainers directly for sensitive issues

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Annual contributor appreciation posts

Thank you for helping make cybersecurity threat intelligence more accessible!
