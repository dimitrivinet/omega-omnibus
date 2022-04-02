# omega-omnibus

Yann and Dimitri's incredible cross-platform omnibus project.

# What is Omnibus ?

# Setup

## Requirements

- git
- Python >= 3.10 (conda recommended)

Optional:
- GNU Make

## Installation

- Clone git repository and cd into it:

```bash
git clone https://github.com/dimitrivinet/omega-omnibus
cd omega-omnibus
```

(Recommended)
- Create and activate conda environment:

```bash
conda create -n omega_omnibus python=3.10
conda activate omega_omnibus
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

### For developpment:

- Install dev dependencies:

```bash
pip install -r requirements-dev.txt
```

- Install pre-commit:

```bash
pre-commit install
```

## Contributing

### Commit and push

#### Add files

To add a file to commit:

```bash
git add <file path>
```

To add all files:

```bash
git add -A
```

#### Commit changes

```bash
git commit -am "<message>"
```

#### Push changes

```bash
git push
```
