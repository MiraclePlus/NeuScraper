# NeuScraper

Source code for our ACL'24 paper :
***[Cleaner Pretraining Corpus Curation with Neural Web Scraping](https://arxiv.org/abs/2402.14652)***

If you find this work useful, please cite our paper  and give us a shining star.

## Quick Start

**1️⃣ Download checkpoint for NeuScraper**

```bash
git lfs install
git clone https://huggingface.co/OpenMatch/neuscraper-v1-clueweb
```

**2️⃣ Clone from git**

```bash
git clone https://github.com/MiraclePlus/NeuScraper
cd NeuScraper
```

**3️⃣ Environment**

Install the `torch` first :

```bash
pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
```

Install other packages :

```bash
pip install -r requirements.txt
```

**4️⃣ Install As Package**

Install the `neu_scraper` package :

```bash
pip install -e .
```

You also can install from whl :

```bash
python setup.py bdist_wheel
pip install dist/neu_scraper-0.1-py3-none-any.whl
```

**5️⃣ Use it like**

```python
from neu_scraper import predict
import requests

url = 'https://blog.christianperone.com/2023/06/appreciating-llms-data-pipelines/'
model_path = '../neuscraper-v1-clueweb/training_state_checkpoint.tar'

response = requests.get(url)
html = response.content.decode('utf-8')

result = predict(html, url, model_path)
print(result)
```

## Citation

```
@inproceedings{xu2024cleaner,
  title={Cleaner Pretraining Corpus Curation with Neural Web Scraping},
  author={Xu, Zhipeng and Liu, Zhenghao and Yan, Yukun and Liu, Zhiyuan and Xiong, Chenyan and Yu, Ge},
  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
  year={2024}
}
```

## Contact Us

If you have questions, suggestions, and bug reports, please send a email to us, we will try our best to help you.

```bash
xuzhipeng@stumail.neu.edu.cn
```
