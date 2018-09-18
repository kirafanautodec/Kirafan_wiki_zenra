<?php
  $token = file_get_content('.secret');
  $body = file_get_contents('php://input');
  $post = json_decode($body, true);
  if (!isset($_SERVER['HTTP_X_HUB_SIGNATURE'])) {
    header('HTTP/1.1 400 Bad Request');
    die('wrong token');
  } else {
    $sha1 = hash_hmac('sha1', $body, $token);
    header('sha1'.$sha1.':'.$_SERVER['HTTP_X_HUB_SIGNATURE']);
    if ('sha1='.$sha1 !== $_SERVER['HTTP_X_HUB_SIGNATURE']) {
      header('HTTP/1.1 400 Bad Request');
      die('wrong token');
    }
  }
  if (!isset($_SERVER['HTTP_X_GITHUB_EVENT']) || $_SERVER['HTTP_X_GITHUB_EVENT'] !== 'push') {
    exit('not push');
  }
  if (!isset($post['ref']) || $post['ref'] !== 'refs/heads/master') {
    exit('ignore');
  }
  $ret = shell_exec('screen -dm bash -c "./deploy.js deploy 2>&1 | tee deploy.log"');
  echo $ret;
