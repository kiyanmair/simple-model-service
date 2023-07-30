test-model:
	@export $(shell grep -v '^#' env/test.env | xargs) && \
	cd model && pytest
