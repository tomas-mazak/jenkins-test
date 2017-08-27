Jenkins Github Integration
==========================

[![Build Status](https://jenkins.rack.valec.net/buildStatus/icon?job=jenkins-test_master_build)](https://jenkins.rack.valec.net/job/jenkins-test_master_build)

This is a testing repo for Jenkins - Github integration.


What's working
--------------

  - automated builds of master branch on push
  - producing build status shields.io badge (see above)
  - automated builds of pull requests with reporting (changes commit status)
  - coverage reporting of pull requests (adds a comment), comparison with master


What's missing
--------------

  - shields.io badge for code coverage (couldn't find the right Jenkins module)

How to setup
------------

1. Install jenkins and following plugins:
  - GitHub
  - embeddable-build-status
  - GitHub Pull Request Builder
  - Cobertura Plugin
  - GitHub Pull Request Coverage Status
2. Configure webhooks (Manage Jenkins -> Configure System)
  - for GitHub plugin (push only)
  - for GitHub PR Builder plugin (issue comment, pull request)
3. Setup 2 jobs:
  - Master build (GitHub triggered)
  - PR build (GitHub PR Builder triggered)
4. Add post-build actions for master build:
  - Publish Cobertura Coverage Report
  - Record Master Coverage
5. Add post-build actions for PR build:
  - Publish Cobertura Coverage Report
  - Publish coverage to GitHub

Links
-----

  - https://www.theguild.nl/building-github-pull-requests-with-jenkins/
  - https://github.com/jenkinsci/github-pr-coverage-status-plugin/blob/master/README.md
  - https://wiki.jenkins.io/display/JENKINS/Embeddable+Build+Status+Plugin
