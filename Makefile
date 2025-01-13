# Makefile for installing dependencies

# Target for upgrading pip and installing dependencies
install:
	# Upgrade pip
	python -m ensurepip --upgrade
	python -m pip install --upgrade pip
	
	# Install dependencies from requirements.txt
	pip install -r requirements.txt

# You can also add a clean target if you want to clear cached files
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache