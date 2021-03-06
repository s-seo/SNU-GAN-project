# GAN Project

Generating image data for research/learning applying the Generative Adversarial Network

## Authors

![image-20210307032254774](C:\Users\baoro\AppData\Roaming\Typora\typora-user-images\image-20210307032254774.png)

## File Summary

#### 1. data

> * A requirements file (txt) and .py for downloading ISIC image files.
> * ISICArchive_Detail.csv : data description

#####  Prerequisites

```
Python >= 3.7.3
```

##### Data installing

```
git clone https://github.com/s-seo/SNU-GAN-project
```

```
cd SNU-GAN-project
```

```
pip install -r ISIC_file_requirements.txt
```

```
python ISIC_image_down.py
```

```
python ISIC_detail_down.py
```

#### 2. engine

> * CNN : CNN modeling 
> * DCGAN : DCGAN modeling
> * GAN : GAN modeling