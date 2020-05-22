FROM python:3

ADD ./sort_two_lists.py /
ADD ./bootstrap.sh /

ENTRYPOINT ["./bootstrap.sh"]
