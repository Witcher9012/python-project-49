install:
		poetry install

brain-games:
		poetry run brain-games
		
build:
		poetry build

publish:
		poetry publish

package-install:
		python3 -m pip install --user dist/*.whl