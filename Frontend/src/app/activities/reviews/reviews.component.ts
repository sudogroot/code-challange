import {Component, OnInit} from '@angular/core';
import {ReviewsService} from './reviews.service';
import {finalize} from 'rxjs/operators';
import {CookieService} from 'ngx-cookie-service';
import {Router} from '@angular/router';


@Component({
  selector: 'app-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.scss']
})
export class ReviewsComponent implements OnInit {


  comments: any;
  stars: any;
  starsLoading: boolean;
  commentsLoading: boolean;
  cookieExists: boolean = this.cookieService.check('user_name');


  constructor(private reviewsService: ReviewsService, private cookieService: CookieService, private router: Router) {
  }

  ngOnInit() {
    this.getComments();
    this.getStars();
  }

  getComments(page: string = '') {
    this.commentsLoading = true;
    this.reviewsService.getComments(page)
      .pipe(finalize(() => {
        this.commentsLoading = false;
      }))
      .subscribe((r: any) => {
        this.comments = r;

      });
  }

  getStars(page: string = '') {
    this.starsLoading = true;
    this.reviewsService.getStars(page)
      .pipe(finalize(() => {
        this.starsLoading = false;
      }))
      .subscribe((r: any) => {
        this.stars = r;

      });
  }

  navigate(event: any, isbn: string) {
    event.preventDefault();
    this.router.navigate(['../../book', isbn]);
  }

}
