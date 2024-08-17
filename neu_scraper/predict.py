import os
import torch
from .builder import build
from .extractor import inference, save_predictions, get_text_spans_from_nodes
from .extractor import ContentExtractionDeepModel
from .arguments import create_parser

ref_model_path = os.getenv('MODEL_PATH')
ref_model = None
ref_args = None

def init_model(model_path):
    parser = create_parser()
    args, _ = parser.parse_known_args()
    args.model_path = model_path
    args.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = ContentExtractionDeepModel(args)
    return model, args

def predict(html, url, model_path = None):
    global ref_model, ref_args, ref_model_path
    if ref_model is None:
        ref_model, ref_args = init_model(model_path or ref_model_path)

    model = ref_model
    args = ref_args

    content = html.encode('UTF-8')
    text_nodes_df, data = build(url, content)

    pred_nodes = inference(args, model, data)
    pred_nodes_df = save_predictions(pred_nodes)

    pred_df = get_text_spans_from_nodes(text_nodes_df, pred_nodes_df).dropna().sort_values(['TextNodeId'], ascending=[False])
    pred_df = pred_df.groupby(['Url', 'Task'], as_index=False).agg({ 'Text': ''.join })

    return { 'Text': pred_df['Text'][0] }