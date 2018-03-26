import {Component, OnInit} from '@angular/core';
import {UserActivitiesService} from './user-activities.service';
import {finalize} from 'rxjs/operators';
import {CookieService} from 'ngx-cookie-service';
import {Router} from '@angular/router';


@Component({
  selector: 'app-user-activities',
  templateUrl: './user-activities.component.html',
  styleUrls: ['./user-activities.component.scss']
})
export class UserActivitiesComponent implements OnInit {


  comments: any;
  stars: any;
  starsLoading: boolean;
  commentsLoading: boolean;
  cookieExists: boolean = this.cookieService.check('user_name');


  constructor(private userActService: UserActivitiesService,
              private cookieService: CookieService, private router: Router) {
  }

  ngOnInit() {
    this.getComments();
    this.getStars();
  }

  getComments(page: string = '') {
    this.commentsLoading = true;
    this.userActService.getComments(page)
      .pipe(finalize(() => {
        this.commentsLoading = false;
      }))
      .subscribe((r: any) => {
        this.comments = r;

      });
  }

  getStars(page: string = '') {
    this.starsLoading = true;
    this.userActService.getStars(page)
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
