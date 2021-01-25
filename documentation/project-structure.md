# Project Structure

1. [Folders](#folders)
    1. [Frontend](#frontend)
2. [Files](#files)

## Folders

**api**

Folder containing API files for each domain of the application. Try to sub-divide your REST API space into separate 
 files to keep things manageable.
 
> Recommendation: for other file names: `site_api.py`, `image_api.py`, ... defining `register_endpoint(app, stores)` 
 functions

**documentation**

Folder containing Markdown files describing various aspects of the project.

> Recommendation: link Markdown files in the main `README.md`

**frontend**

Main React application code. See [Frontend](#frontend) for details.

> Note, that some frontend-related files are also produced in the `/static` folder and additional front-end related files
 are listed in the [Files](#files) section.

**node_modules**

Folder produced by `npm` (the JavaScript package manager) to store dependencies required to build the front-end.

**static**

Static folder containing resources delivered to the browser via `http://<host>:<port>/statric/*` by Flask. This folder 
 will be used by `webpack` (a JavaScript build tool) to compile the front-end as `index.js`, which will contain the 
 entire frontend.
 
> You can also use this folder to store images in a sub-directory `/static/images/`, which is already added to the 
 exception list of `.gitignore`. You can add additional folders, if you require (e.g. `/static/download`), but remember 
 you have to explicitly add them to the `.gitignore` - e.g. `!/static/images/*`

**storage**

Folder containing database store classes and DB objects. 

> Recommendation: create a file for each store, and suffix the file name with `_store`, e.g. `site_store.py`, 
 `template_store.py`, ... defining a store class (camel-case with capital letter first, ending in `...Store) and a 
 de-serialised class representing objects in the collection or table. There are mechanisms integrated in `pbu` to 
 de-serialise from MongoDB (`dict`) or MySQL (`list`). Examples: `SiteStore` with de-serialise class `Site`.

**templates**

A folder created by `webpack` (a JavaScript build tool), where it stores the `index.html`, which is the main entry point
 for any request via the browser and will include an injected `<script>` call to the compiled front-end in the `/static` 
 directory. This file is generated, as the include-path for the `index.js` is dynamic.

**_logs**

The main log folder used by the `pbu` pip library to store log files from the `pbu.Logger`

**_data**

If you use Frappy (`frappyflaskdataset`) and want to store images, this is the default folder, where Frappy will store
 images as files.

### Frontend

**index.html**

The main entry point for the front-end, is the `index.html`, which gets delivered by Flask (not exactly, because Webpack
 injects the `<script>` tag for the `index.js` and copies the file into the `/templates` folder, which is the default 
 Flask folder for the `index.html`).
 
**src/index.js**

This is the main programming entry point for the React application. This is the script that gets loaded and executed 
 first when the front-end is loaded by the browser.
 
It is using JSX syntax and describes the front-end routes available for the application. Please note that each route 
 corresponds to an entry in the `api/static_api.py`. If you add additional routes, please remember to add them also to
 the `api/static_api.py` endpoints.
 
**src/containers**

"Containers" are React components that represent larger entities, e.g. entire pages (but also smaller, self-sufficient
 components included in other pages). They will most likely have a state and facilitate API access and delegate the 
 rendering to sub-components and only provide a scaffolding for the layout of the component / page.
 
**src/components**

This folder doesn't exist yet. I recommend creating it, so you can store smaller re-usable components. You should also
 consider breaking up your larger container, if it does a lot of rendering, passing properties from the container to the
 smaller component.
 
> Recommendation: This folder should have sub-folders for various domains or type of components (list components, form
 components or site-related components, image-related components). React components should rarely exceed 200-300 
 (linted) lines of code.
>  
> You can have files on the root of this folder - this is a good place for generic components such as `Header.js` or 
 `Menu.js`.

**src**

Main source folder for the JavaScript code.

> Recommendation: create files here like `common.js`, which define commonly used objects or functions across the
 components. This can also be utility functions. Another use would be to have a `mixins.js` file with styles and colour 
 schemes used across components. You can also have a file called `theme.js` for the colour scheme.   

## Files

**runner.py**

The main start script for the application

**config.py**

The configuration file for the backend, which connects the OS environment variables with the application configuration.

**.babelrc**, **package.json**, package-lock.json**, **webpack.config.js**

Configuration files for:

- _NPM_ (package.json files) - the JavaScript package manager - defines dependencies
- _Babel_ - a JavaScript language extension allowing for ES6 syntax
- _Webpack_ - a JavaScript bundler that compiles the front-end into a single resource for the browser

**.eslintignore**, **.eslintrc.json**

ESLint is a linter for JavaScript and provides a rule-set and ignore rules.

**setup.cfg**, **requirements.txt**

Python configuration files defining editor rules (`setup.cfg`) and pip dependencies. 

**.env.template**

This file is meant as a template for a `.env` file, which is used to individually configure your app without committing 
 the configuration to Git.
 
> Recommendation: copy the file to `.env` and adjust the variables there. When you add new configuration variables (see
 also the `config.py`), make sure to also add them to the `.env.template` file with a "default" or dummy value. Do not 
 leave actual credentials in there.
