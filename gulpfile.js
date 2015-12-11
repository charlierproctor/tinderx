var gulp = require('gulp');

var concat = require('gulp-concat')
var using = require('gulp-using')
var sass = require('gulp-sass')
var bowerFiles = require('main-bower-files')
var angularFilesort = require('gulp-angular-filesort')
var bower = require('gulp-bower')
var del = require('del')

var paths = {
  html: [
  	'app/**/*.html',
  	'!app/bower_components/**/*.html'
  ],
  sass: [
  	'app/css/*.scss'
  ],
  css: [
    'app/bower_components/pure/pure-min.css'
  ],
  img: [
  	'app/img/**/*'
  ],
  scripts: [
    'app/**/*.js',
    '!app/bower_components/**/*.js'
  ],
  libs: [],
  static: [
    'app/static/**/*'
  ]
};

gulp.task('bower', function() {
  return bower()
})
gulp.task('clean', function(cb) {
  del([
    'dist/'
  ], cb)
})
gulp.task('html', ['bower','clean'], function() {
	return gulp.src(paths.html)
	.pipe(using())
	.pipe(gulp.dest('dist'))
})
gulp.task('sass', ['bower','clean'], function() {
	return gulp.src(paths.sass)
  .pipe(using())
  .pipe(sass())
	.pipe(gulp.dest('dist'))
})
gulp.task('css', ['bower','clean'], function() {
  return gulp.src(paths.css)
  .pipe(using())
  .pipe(concat('lib.css'))
  .pipe(gulp.dest('dist'))
})
gulp.task('img', ['bower','clean'], function() {
	return gulp.src(paths.img)
  .pipe(using())
	.pipe(gulp.dest('dist/img'))
})
gulp.task('static', ['bower','clean'], function() {
  return gulp.src(paths.static)
  .pipe(using())
  .pipe(gulp.dest('dist/static'))
})
gulp.task('vendor', ['bower','clean'], function() {
	return gulp.src(bowerFiles({
    "overrides":{
      "pure": {
        ignore: true
      }
    }
  }).concat(paths.libs))
  .pipe(using())
	.pipe(concat('lib.js'))
	.pipe(gulp.dest('dist'));
})
gulp.task('scripts', ['bower','clean'], function() {
  return gulp.src(paths.scripts)
  	.pipe(angularFilesort())
    .pipe(using())
  	.pipe(concat('app.js'))
    .pipe(gulp.dest('dist'));
});

gulp.task('all', ['html','sass','css','img','vendor','scripts','static'])
gulp.task('default', ['all']);

gulp.task('watch', ['all'], function() {
  var all = paths.html.concat(paths.sass).concat(paths.css).concat(paths.img).concat(paths.scripts).concat(paths.static)
  gulp.watch(all, ['all']);
});
