# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from entity_classifier import EntityClassifier
import os
from glob import glob
import json


def readlines(path, pattern='*.txt'):
    full_path = os.path.join(path, pattern)
    for fname in glob(full_path):
        for line in open(fname, 'r'):
            yield line

            
@click.command()
@click.option('patterns', '-p', type=click.Path(exists=True))
@click.argument('input_filepath', type=click.STRING)
@click.argument('output_filepath', type=click.Path())
def main(patterns, input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    print(patterns, input_filepath, output_filepath)
    entity_classifer = EntityClassifier(regex=patterns)
    lines = [
        entity_classifer.get_entities(line)
        for line in readlines(input_filepath)
    ]
    entities = [
        {ent.text: ent.label_}
        for line in lines
        for ent in line.ents
        if ent.label_ == 'PERSON' or ent.label_ == 'IP']
    logger.info(f'found {len(entities)} entities')
    logger.info(f'writing entities to {output_filepath}')
    with open(output_filepath, 'w') as out_file:
        json.dump(entities, out_file)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables

    main()
