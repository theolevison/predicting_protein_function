import time
import os
from tape.models.file_utils import url_to_filename, get_cache, get_etag
from tape import ProteinBertModel
from tape import TAPETokenizer
from tape.models.modeling_bert import BERT_PRETRAINED_MODEL_ARCHIVE_MAP
import torch


def test_forcedownload():
    model = ProteinBertModel.from_pretrained('bert-base')
    url = BERT_PRETRAINED_MODEL_ARCHIVE_MAP['bert-base']
    filename = url_to_filename(url, get_etag(url))
    wholepath = get_cache()/filename
    oldtime = time.ctime(os.path.getmtime(wholepath))
    model = ProteinBertModel.from_pretrained('bert-base', force_download=True)
    newtime = time.ctime(os.path.getmtime(wholepath))
    assert(newtime != oldtime)
    # Deploy model
    # iupac is the vocab for TAPE models, use unirep for the UniRep model
    tokenizer = TAPETokenizer(vocab='iupac')
    # Pfam Family: Hexapep, Clan: CL0536
    sequence = 'GCTVEDRCLIGMGAILLNGCVIGSGSLVAAGALITQ'
    token_ids = torch.tensor([tokenizer.encode(sequence)])
    model(token_ids)
    
"""
import tape
tape.

tape-train-distributed transformer secondary_structure \
	--from_pretrained results/<path_to_folder> \
	--batch_size BS \
	--learning_rate LR \
	--fp16 \
  	--warmup_steps WS \
  	--nproc_per_node NGPU \
  	--gradient_accumulation_steps NSTEPS \
  	--num_train_epochs NEPOCH \
  	--eval_freq EF \
  	--save_freq SF
"""