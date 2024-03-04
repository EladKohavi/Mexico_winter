#!/bin/bash

version=$(git describe --tags --abbrev=0 || echo '0.0.0')
echo "version: $version"

# Check if the version starts with 'v' and remove it
if [[ $version == v* ]]; then
    version=${version:1}
fi

IFS='.' read -r -a versions <<< "$version"

major=${versions[0]}
minor=${versions[1]}
patch=${versions[2]}

# Increment the patch version
patch=$((patch + 1))

# Create the new tag
new_tag="v${major}.${minor}.${patch}"
echo "new tag: $new_tag"

git tag $new_tag
git push origin $new_tag