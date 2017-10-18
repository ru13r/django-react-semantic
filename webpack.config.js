const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const autoprefixer = require('autoprefixer');
// let BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

const loaders = {
    css: {
        loader: 'css-loader'
    },
    postcss: {
        loader: 'postcss-loader',
        options: {
            plugins: (loader) => [
                autoprefixer({
                    browsers: ['last 2 versions']
                })
            ]
        }
    },
    sass: {
        loader: 'sass-loader',
        options: {
            indentedSyntax: true,
            includePaths: [path.resolve(__dirname, './src')]
        }
    },
    less: {
        loader: 'less-loader'
    }
};

const config = {

        entry: {
            base: [
                'webpack-dev-server/client?http://localhost:3000',
                'webpack/hot/only-dev-server',
                './assets/js/base.js', // base chunk includes common libraries
            ],
            react_test: [
                'webpack-dev-server/client?http://localhost:3000',
                'webpack/hot/only-dev-server',
                'react-hot-loader/patch',
                './assets/js/react_test.js'
            ]
        },

        module: {
            rules: [
                {
                    test: /\.jsx?$/,
                    exclude: /node_modules/,
                    use: [{
                        loader: 'babel-loader',
                        options: {
                            babelrc: false,
                            presets: [
                                ['env', {
                                    'targets': {
                                        'browsers': [
                                            '> 1%',
                                            'last 2 versions']
                                    },
                                    'debug': true,
                                }],
                                'react'
                            ]
                        }
                    }]
                },
                {
                    test: /\.sass$/,
                    use: ['css-hot-loader'].concat(ExtractTextPlugin.extract({
                        fallback: 'style-loader',
                        use: [loaders.css, loaders.postcss, loaders.sass]
                    }))
                    // use: ['style-loader', 'css-loader', 'sass-loader'],
                },
                {
                    test: /\.css$/,
                    use: ['css-hot-loader'].concat(ExtractTextPlugin.extract({
                        fallback: 'style-loader',
                        use: loaders.css
                    }))
                    // use: ['style-loader', 'css-loader'],
                },
                {
                    test: /\.less/,
                    use: ['css-hot-loader'].concat(ExtractTextPlugin.extract({
                        fallback: 'style-loader',
                        use: [loaders.css, loaders.postcss, loaders.less]
                    }))
                },
                {
                    test: /\.(png|jpg|gif|woff|svg|eot|ttf|woff2)$/,
                    loader: 'url-loader?limit=1024&name=[name]-[hash:6].[ext]!image-webpack-loader',
                },
            ]
        },

        output: {
            path: path.resolve('./assets/bundles/'),
            filename: '[name].js',
            publicPath: 'http://localhost:3000/assets/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name

        },

        plugins: [
            new webpack.HotModuleReplacementPlugin
            (),
            new ExtractTextPlugin('[name].css'),
            new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
            new BundleTracker({filename: './webpack-stats.json'}),
            new webpack.ProvidePlugin({
                $: 'jquery',
                jQuery: 'jquery'
            }),
            // new BundleAnalyzerPlugin({
            //     analyzerMode: 'static'
            // }),
        ],

        resolve:
            {
                modules: [path.join(__dirname, './assets'), 'node_modules', 'bower_components'],
                extensions:
                    ['.js', '.jsx', '.sass']
            }
        ,
    }
;

module.exports = config;