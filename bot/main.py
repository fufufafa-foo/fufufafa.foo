import os
import random
import re

import praw
from dotenv import load_dotenv

# Load env
load_dotenv()
bot_name = os.getenv("BOT_NAME")
keywords = os.getenv("KEYWORDS").split(",")
subreddits = os.getenv("SUBREDDITS")
log_file = "./logs.txt"

# Init bot
reddit = praw.Reddit(bot_name, config_interpolation="basic")


# Function definitions
def read_logs():
  if not os.path.isfile(log_file):
    return []
  else:
    with open(log_file, "r") as f:
      return f.read().splitlines()


def write_logs(logs, comment):
  print("comment: " + comment.id + " \"" + comment.body + "\"")
  logs.append(comment.id)
  with open(log_file, "a") as f:
    f.write(comment.id + "\n")


def parse_quote(s):
  pattern = r'\s+https:\/\/[^\s]+'
  return re.sub(pattern, '', s).replace('|', '').strip()


def exclude_quotes(s):
  excluded_keywords = ["(cerita prabowo mendaki semeru)", "(pantun)"]
  return all([x not in s for x in excluded_keywords])


def read_quotes():
  l = list()
  raw_files = ["list.txt", "list-2.txt"]
  for file in raw_files:
    with open("../raw/" + file, "r") as f:
      l.extend(list(map(parse_quote, f.read().splitlines())))
  return list(set(filter(exclude_quotes, l)))


def get_random_quote():
  quotes = read_quotes()
  return random.choice(quotes)


def reply(comment):
  quote = get_random_quote()
  print("Replying with \"" + quote + "\"...")
  comment.reply(quote)


def main():
  comments = read_logs()
  print(f"Starting {bot_name}")
  try:
    for comment in reddit.subreddit(subreddits).stream.comments():
      for keyword in keywords:
        if keyword in comment.body.lower() and comment.id not in comments:
          write_logs(comments, comment)
          reply(comment)
  except Exception as e:
    print("Exception caught: ")
    print(e)
    main()


# Run bot
main()
