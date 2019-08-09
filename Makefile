PROJECT_NAME?=mixit_365talents
#
PACKAGE_NAME=$(shell python setup.py --name)
PACKAGE_FULLNAME=$(shell python setup.py --fullname)
PACKAGE_VERSION:=$(shell python setup.py --version)
#
#DOCKER_TAG?=$(PROJECT_NAME):${PACKAGE_VERSION}
#
# https://stackoverflow.com/questions/2019989/how-to-assign-the-output-of-a-command-to-a-makefile-variable
PYPI_SERVER?=
PYPI_SERVER_HOST?=
PYTEST_OPTIONS?=-v
#
TOX_DIR?=.tox
#
SDIST_PACKAGE=dist/${shell python setup.py --fullname}.tar.gz
SOURCES=$(shell find src/ -type f -name '*.py') setup.py MANIFEST.in

#all: docker

${SDIST_PACKAGE}: ${SOURCES}
	@echo "Building python project..."
	@python setup.py sdist

pypi-register:
	python setup.py register -r $(PROJECT_NAME)

pypi-upload: pypi-register
	python setup.py sdist upload -r $(PROJECT_NAME)

pip-install:
	@pip install \
		-r requirements_dev.txt \
		--trusted-host $(PYPI_SERVER_HOST) \
		--extra-index-url $(PYPI_SERVER) \
		--upgrade

re: fclean all

# https://stackoverflow.com/questions/10722723/find-exec-echo-missing-argument-to-exec
fclean:
#	@find . -name "*.pyc" -exec git rm --cached {} \;
	@find . -name "*.pyc" -delete;
	@find . -name "__pycache__" -delete

pytest:
	pytest ${PYTEST_OPTIONS}

tox:
	# http://ahmetdal.org/jenkins-tox-shebang-problem/
	tox --workdir ${TOX_DIR}

#docker: ${SDIST_PACKAGE}
#	@echo PYPI_SERVER: $(PYPI_SERVER)
#	@docker build \
#		--build-arg PYPI_SERVER=$(PYPI_SERVER) \
#		-t $(DOCKER_TAG) \
#		-f docker/Dockerfile \
#		.
#
#docker-run:
#	@docker run --rm -it ${DOCKER_RUN_OPTIONS} $(DOCKER_TAG)
#
#docker-run-shell:
#	@docker run --rm -it ${DOCKER_RUN_OPTIONS} --entrypoint sh $(DOCKER_TAG)

#default: docker