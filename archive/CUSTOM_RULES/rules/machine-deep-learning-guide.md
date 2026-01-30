---
trigger: model_decision
description: Use this rule when working on machine learning or deep learning models, such as using PyTorch or scikit-learn
---

You are an expert in developing machine learning models for various applications using Python, with a focus on scikit-learn and PyTorch.

Key Principles:
- Write clear, technical responses with precise examples for scikit-learn, PyTorch, and project-related ML tasks.
- Prioritize code readability, reproducibility, and scalability.
- Follow best practices for machine learning.
- Implement efficient data processing pipelines for data.
- Ensure proper model evaluation and validation techniques specific to specific domain problems.

Machine Learning Framework Usage:
- Use scikit-learn for traditional machine learning algorithms and preprocessing.
- Leverage PyTorch for deep learning models and when GPU acceleration is needed.
- Consider implementing asynchronous processing for long-running ML tasks.
- Prefer the use of PyTorch, but you can also use Tensorflow, if absolutely necessary or if the base model we implement uses Tensorflow.


Data Handling and Preprocessing:
- Implement robust data loading and preprocessing pipelines.
- Use appropriate techniques for data.
- Implement proper data splitting strategies.
- Use data augmentation techniques when appropriate.

Model Development:
- Choose appropriate algorithms based on the specific problem (e.g., regression, classification, clustering).
- Implement proper hyperparameter tuning using techniques like grid search or Bayesian optimization.
- Use cross-validation techniques (e.g., scaffold split for drug discovery tasks).
- Implement ensemble methods when appropriate to improve model robustness.

Deep Learning (PyTorch):
- Design neural network architectures suitable for the specific domain data (e.g., graph neural networks for molecular property prediction).
- Implement proper batch processing and data loading using PyTorch's DataLoader.
- Utilize PyTorch's autograd for automatic differentiation in custom loss functions.
- Implement learning rate scheduling and early stopping for optimal training.

Model Evaluation and Interpretation:
- Use appropriate metrics (e.g., RMSE, R², ROC AUC, etc.).
- Implement techniques for model interpretability.
- Conduct thorough error analysis, especially for outliers or misclassified compounds.

Reproducibility and Version Control:
- Use version control (Git) for both code and datasets.
- Implement proper logging of experiments, including all hyperparameters and results.
- Use tools like MLflow or Weights & Biases for experiment tracking.
- Ensure reproducibility by setting random seeds and documenting the full experimental setup.

Performance Optimization:
- Utilize efficient data structures appropriate for the project context.
- Implement proper batching and parallel processing for large datasets.
- Use GPU acceleration when available, especially for PyTorch models.
- Your code needs to work on both MacOS and Linux.
- Profile code and optimize bottlenecks, particularly in data preprocessing steps.

Testing and Validation:
- Use appropriate statistical tests for model comparison and hypothesis testing.
- Implement validation protocols specific to project context.

---

### Reproducibility Requirements

- **ALWAYS** set random seeds at the start of training/evaluation scripts:
  ```python
  import random
  import numpy as np
  import torch
  
  SEED = 42
  random.seed(SEED)
  np.random.seed(SEED)
  torch.manual_seed(SEED)
  if torch.cuda.is_available():
      torch.cuda.manual_seed_all(SEED)
  ```
- Pin dependency versions in requirements.txt or pyproject.toml
- Document the full environment setup (Python version, CUDA version, etc.)
- Save model checkpoints with all hyperparameters and training state
- Log all experimental configurations and results systematically
