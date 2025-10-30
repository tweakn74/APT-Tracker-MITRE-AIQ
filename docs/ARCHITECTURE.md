# Architecture Overview

## System Architecture

The APT Tracker is a client-side web application designed for simplicity, performance, and ease of deployment.

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                    APT Tracker Dashboard                    │
├─────────────────────────────────────────────────────────────┤
│  Frontend (Vanilla HTML/CSS/JavaScript)                    │
│  ├── index.html (Main application)                         │
│  ├── Embedded JSON Database (APT Intelligence)             │
│  ├── Interactive Filtering & Search                        │
│  └── Dynamic Content Rendering                             │
├─────────────────────────────────────────────────────────────┤
│  Testing & Quality Assurance                               │
│  ├── Playwright (End-to-end testing)                       │
│  ├── JSON Schema Validation (AJV)                          │
│  └── Automated Link Checking                               │
├─────────────────────────────────────────────────────────────┤
│  CI/CD Pipeline (GitHub Actions)                           │
│  ├── Automated Testing                                     │
│  ├── Schema Validation                                     │
│  └── GitHub Pages Deployment                               │
└─────────────────────────────────────────────────────────────┘
```

### Design Principles

1. **Zero Build Step**: Pure HTML/CSS/JavaScript for maximum compatibility
2. **Embedded Data**: JSON database included in the application for offline capability
3. **Client-Side Only**: No server-side dependencies or API calls required
4. **Progressive Enhancement**: Works without JavaScript, enhanced with it
5. **Mobile-First**: Responsive design for all device types

### Data Architecture

#### APT Database Structure
```javascript
const aptDatabase = {
  "APT_GROUP_NAME": {
    name: "string",
    aliases: ["string"],
    description: "string",
    origin: "string",
    firstSeen: "string",
    targetIndustries: ["string"],
    targetRegions: ["string"],
    motivation: "string",
    sophistication: "enum",
    mitreAttackTechniques: [
      {
        id: "T1234",
        name: "Technique Name",
        tactic: "Tactic Name"
      }
    ],
    attackChain: [
      {
        phase: "string",
        description: "string",
        techniques: ["string"]
      }
    ],
    searchTerms: ["string"],
    attackiqScenarios: [
      {
        name: "string",
        description: "string",
        mitreId: "string"
      }
    ]
  }
};
```

### Frontend Architecture

#### Component Structure
- **Filter Panel**: Dynamic filtering by APT group, industry, and attack type
- **APT Group Cards**: Interactive cards displaying group information
- **Attack Chain Visualization**: Step-by-step attack progression
- **MITRE Technique Mapping**: Visual representation of ATT&CK techniques
- **AttackIQ Integration**: Testable scenarios for each group

#### State Management
- Pure JavaScript with DOM manipulation
- Local storage for user preferences
- URL parameters for shareable filtered views

### Testing Strategy

#### Test Pyramid
1. **Unit Tests**: JSON schema validation
2. **Integration Tests**: Component interaction testing
3. **End-to-End Tests**: Full user workflow validation
4. **Visual Tests**: Screenshot comparison (future enhancement)

#### Test Coverage
- Page load and rendering
- Console error detection
- Data schema validation
- Interactive filtering functionality
- Mobile responsiveness
- Accessibility compliance

### Deployment Architecture

#### GitHub Pages Hosting
```
GitHub Repository
├── Source Code (main branch)
├── GitHub Actions (CI/CD)
├── Automated Testing
├── Build Artifact Generation
└── GitHub Pages Deployment
```

#### CI/CD Pipeline
1. **Trigger**: Push to main branch
2. **Test**: Run Playwright tests
3. **Validate**: JSON schema validation
4. **Build**: Prepare distribution files
5. **Deploy**: GitHub Pages deployment
6. **Verify**: Post-deployment health checks

### Security Considerations

1. **No Sensitive Data**: All data is public threat intelligence
2. **Client-Side Only**: No server-side attack surface
3. **Content Security Policy**: Implemented via meta tags
4. **HTTPS Only**: Enforced by GitHub Pages
5. **No External Dependencies**: Reduced supply chain risk

### Performance Optimization

1. **Minimal Dependencies**: Only essential libraries included
2. **Lazy Loading**: Content loaded on demand
3. **Efficient Filtering**: Optimized search algorithms
4. **Caching Strategy**: Browser caching for static assets
5. **Compression**: Gzip compression via GitHub Pages

### Scalability Considerations

1. **Data Growth**: JSON database can handle hundreds of APT groups
2. **Feature Expansion**: Modular architecture supports new features
3. **User Load**: Static hosting scales automatically
4. **Global Distribution**: CDN via GitHub Pages

### Future Enhancements

1. **Real-time Updates**: Integration with threat intelligence feeds
2. **Advanced Visualization**: D3.js for complex attack chain diagrams
3. **Export Functionality**: PDF/CSV export capabilities
4. **Collaboration Features**: Shared annotations and notes
5. **API Integration**: Direct AttackIQ scenario import
