---
name: Bug report
description: Create a report to help us improve
title: '[Bug] '
labels: ['bug']
assignees: []

body:
  - type: markdown
    attributes:
      value: 'Thanks for taking the time to fill out this bug report!'
  
  - type: textarea
    id: bug-description
    attributes:
      label: Describe the bug
      description: A clear and concise description of what the bug is.
      placeholder: 'e.g. When I do X, Y happens instead of Z.'
    validations:
      required: true
  
  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: Steps to reproduce
      description: How do you trigger this bug?
      placeholder: '1. Go to...'
    validations:
      required: true
  
  - type: textarea
    id: expected-behavior
    attributes:
      label: Expected behavior
      description: What should happen?
    validations:
      required: true
  
  - type: textarea
    id: screenshots
    attributes:
      label: Screenshots
      description: Add any screenshots or videos.
  
  - type: dropdown
    id: labels
    attributes:
      label: Type of bug
      options:
        - UI/UX
        - Performance
        - Logic
        - Other
    validations:
      required: true
