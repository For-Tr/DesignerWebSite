

module.exports = {
    assetsDir: 'static',
    parallel: false,
    publicPath: './',
    devServer: {
        before: function (app) {
            app.use(function(req, res, next) {
                console.log('Proxy request for:', req.url);
                next();
            });
        },
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000/api',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''
                }
            }
        }
    }
};

