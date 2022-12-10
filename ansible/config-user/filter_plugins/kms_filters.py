import boto3
from botocore.config import Config
import base64

cfg = Config(
    region_name='us-east-1'
)
kms = boto3.client('kms', config=cfg)

def kms_decrypt(ciphertext):
    return str(kms.decrypt(CiphertextBlob=base64.b64decode(ciphertext)).get('Plaintext'), 'utf-8')

def kms_encrypt(plaintext, key):
    return str(base64.b64encode(kms.encrypt(KeyId=key,Plaintext=plaintext).get('CiphertextBlob')), 'utf-8')

class FilterModule(object):
    def filters(self):
        return { 'kms_encrypt': kms_encrypt, 'kms_decrypt': kms_decrypt }
