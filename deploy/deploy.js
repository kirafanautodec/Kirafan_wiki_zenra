#!/usr/local/bin/node
require('shelljs/global')
const fs = require('fs')
const path = require('path')

config.fatal = true

const cwd = path.join(__dirname, '..')
const LOCK_FILE = path.join(cwd, '.deploy.lock')

if (fs.existsSync(LOCK_FILE)){
  process.exit(1);
}

let ret = 0
try {
  fs.writeFileSync(LOCK_FILE)
  process.env.PATH += ':/usr/local/bin:/usr/bin'

  exec('env')
  exec('git pull')
  ret = exec('python3 script/build.py', {cwd})

} catch (e) {
  console.error(e)
  ret = 1
} finally {
  fs.unlinkSync(LOCK_FILE)
}

process.exit(ret.code)
