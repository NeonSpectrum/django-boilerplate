const webpack = require('webpack')
const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const BundleTracker = require('webpack-bundle-tracker')

const assetDir = path.resolve(__dirname, '../backend/static/site')

const isDevServer = process.argv.find(v => v.includes('webpack-dev-server'))

module.exports = {
  entry: './index.js',
  output: {
    path: assetDir + '/bundles',
    filename: '[name]-[hash].js',
    publicPath: isDevServer && 'http://localhost:8080/'
  },
  devServer: {
    headers: { 'Access-Control-Allow-Origin': '*' },
    hot: true,
    port: 8080
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new BundleTracker({ filename: assetDir + '/webpack-stats.json' })
  ],
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test: /\.scss$/,
        include: path.resolve(__dirname, 'src/styles/'),
        use: [
          process.env.NODE_ENV !== 'production' ? 'style-loader' : MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader'
          },
          {
            loader: 'sass-loader'
          }
        ]
      }
    ]
  },
  watchOptions: {
    ignored: 'node_modules/'
  },
  resolve: {
    alias: {
      'react-dom': '@hot-loader/react-dom'
    },
    extensions: ['.js', '.jsx', '.json']
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /node_modules/,
          chunks: 'initial',
          name: 'vendor',
          enforce: true
        }
      }
    }
  }
}
