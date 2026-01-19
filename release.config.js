var dryRun = (process.env.RELEASE_DRY_RUN || "false").toLowerCase() === "true";

var publishCmd = `
echo \${nextRelease.version} > VERSION
python -m build
python -m twine upload dist/*
`

if (dryRun) {
    publishCmd = publishCmd.replace("upload", "upload --repository testpypi");
} else {
    // Force the use of the production PyPI repository
    publishCmd = publishCmd.replace("upload", "upload --repository pypi");
}

var config = require('semantic-release-preconfigured-conventional-commits');

config.branches = ['main'];

config.plugins.push(
    [
        "@semantic-release/exec",
        {
            "publishCmd": publishCmd,
        }
    ],
    ["@semantic-release/github", {
        "assets": [ 
            { "path": "dist/*" },
         ]
    }],
    "@semantic-release/git",
)

module.exports = config
