#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Que lo queee Mundo!')
    
if __name__=='__main__':
    hello()