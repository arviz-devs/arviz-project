name: 'Issue Report'
description: Create a report to help us improve www.arviz.org
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this report!
  - type: textarea
    id: what-happened
    attributes:
      label: Describe the problem
      description: A clear and concise description of what the problem is.
      placeholder: Tell us what you see! Please provide both links and screenshots that show what the issue is.
    validations:
      required: true
  - type: textarea
    id: expectation
    attributes:
      label: Expected behaviour
      description: A clear and concise description of what you expected to happen or see.
    validations:
      required: true
  - type: textarea
    id: extra
    attributes:
      label: Additional context
      description: A clear and concise description of what you expected to happen or see.
