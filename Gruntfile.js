const shell = (x) => `$(${x})`;

const kvs = (arr) => Object.fromEntries(arr.map((i) => [i, i]));

const greps = (arr) => arr.reduce((acc, x) => acc + ' | grep ' + x, '');

const less = (x) => ({ cmd: x.concat(' | less -REX'), stdout: 'inherit' });

const merge = (arr) => arr.reduce((x, y) => ({ ...x, ...y }), {});

const parametrize = (name) => (env) =>
  grunt.task.run(['exec', name, env].join(':'));

const changed = (arr = []) =>
  shell('git diff --name-only HEAD '.concat(greps(arr)));

const created = (arr = []) =>
  shell('git status --porcelain | grep "^??" | cut -c 4- '.concat(greps(arr)));

const comprehension = (obj, cb) =>
  Object.fromEntries(Object.entries(obj).map(cb));

const commands = (arr) =>
  arr.reduce(
    (x, y) => x.concat(y.includes(':') ? y : 'exec:'.concat(y)),
    ['clean']
  );

const flakeOptions = `
   -v -ri --exclude 'venv, conftest.py'
   --remove-unused-variables
   --remove-all-unused-imports
   --ignore-init-module-imports
`;

const conductor = {
  alphabetize: 'conductor cspell format',
  missing: 'conductor cspell words',
};

const linters = {
  cspell: 'npx cspell ".*" "*" "**/*"',
  mypy: `mypy . --exclude '(src/core|e2e/cases|venv)'`,
  pylint: 'pylint --rcfile .pylintrc  --fail-under=8 src tests',
  remark: 'npx remark -r .remarkrc --ignore-path .gitignore . .github',
};

const formatters = {
  autoflake: `autoflake . ${flakeOptions}`,
  black: 'black .',
  isort: 'isort .',
};

const tests = {
  tox: 'tox . -e py',
};

const clean = kvs(['dist']);

const exec = merge([linters, formatters, tests]);

module.exports = (grunt) => {
  grunt.initConfig({ clean, exec });

  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-exec');

  grunt.registerTask(
    'lint',
    'Lint the source code.',
    commands(['cspell', 'pylint', 'mypy', 'remark'])
  );

  grunt.registerTask(
    'format',
    'Format the source code.',
    commands(['autoflake', 'black', 'isort'])
  );

  grunt.registerTask('test', 'Run unit tests.', commands(['tox']));
};
