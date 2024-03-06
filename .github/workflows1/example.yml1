name: example
on:
  workflow_dispatch:
    inputs:
      commit_sha:
        description: 'Commit sha to run for workflow'
        required: false
jobs:
  job_1:
    runs-on: ubuntu-latest
    steps:
      - name: My first step
        run: |
          echo This is the first step of my first job. 
          echo client_payload '${{ github.event.inputs.client_payload }}'
          sleep 1m
