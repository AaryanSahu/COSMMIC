# COSMMIC: Comment-Sensitive Multimodal Multilingual Indian Corpus

**COSMMIC** (Comment-Sensitive Multimodal Multilingual Indian Corpus) is the **first large-scale dataset** designed for **summarization and headline generation** across **nine major Indian languages**, with a focus on **reader feedback integration**. This dataset bridges the gap in multimodal and multilingual resources for Indian NLP, incorporating **text, user comments, and images** to support more contextual and diverse Natural Language Generation (NLG).

---

## 🗃 Dataset Structure


Each language folder includes:
- `SUMMARY/`: Ground-truth summaries per article
- `HEADLINE/`: Ground-truth headlines

---

## 🔍 Key Features

- **Languages**: Bengali, Hindi, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, English
- **Size**: 4,959 article-image pairs and 24,484 comments
- **Multimodal**: Each article is associated with an image
- **Comment-Sensitive**: Reader comments enhance contextual summarization
- **Annotations**: Human-curated summaries and headlines across all languages

---

## 🧠 Research Contributions

1. **Multilingual + Multimodal Integration**  
   Unified dataset incorporating **article text, images, and user comments**.

2. **Comment-Aware Summarization**  
   Filters and identifies **supportive and noise-free comments** using a fine-tuned **IndicBERT classifier**.

3. **Image Utility in NLG**  
   Employs **multilingual CLIP** to extract semantic insights from images.

4. **Evaluation across 4 Configurations**:
   - Article text only  
   - Article + Comments  
   - Article + Image  
   - Article + Comments + Image

5. **Baseline and Benchmarking**  
   Evaluation using **LLama3**, **GPT-4**, and other SOTA models for headline generation and summarization.

---

## 🛠 Tools Used

- 🧠 **IndicBERT**: For comment classification
- 🖼 **Multilingual CLIP**: Image-based feature extraction
- 🤖 **LLama3**, **GPT-4**: NLG benchmark models
- 📊 Custom metrics for evaluating comment utility and summarization quality

---


## 📚 Citation

If you use COSMMIC in your research, please cite:

```bibtex
@inproceedings{your2025cosmmic,
  title={COSMMIC: A Comment-Sensitive Multimodal Multilingual Corpus for Indian Language Summarization},
  author={Raghvendra Kumar, Mohammed Salman S A, Aryan Sahu, Tridib Nandi, Pragathi Y P, Sriparna Saha, Jose G Moreno},
  booktitle={Proceedings of ACL 2025},
  year={2025}
}
```

---

## 📬 Contact

For questions or collaborations, feel free to reach out:

* Aryan Sahu: [aryansahu010103@gmail.com](mailto:aryansahu010103@gmail.com)
* GitHub Issues: [Submit here](https://github.com/your-org/cosmmic-dataset/issues)

---

## 🌏 Towards Inclusive NLP

COSMMIC enables fair and rich modeling across diverse linguistic communities in India. We believe in fostering **inclusive, accessible AI** for all.

