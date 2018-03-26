import {Component, OnInit} from '@angular/core';
import {ActivitiesService} from './activities.service';
import {BookList} from '@app/models/book';
import {finalize} from 'rxjs/operators';
import {CookieService} from 'ngx-cookie-service';



@Component({
  selector: 'app-activities',
  templateUrl: './activities.component.html',
  styleUrls: ['./activities.component.scss']
})
export class ActivitiesComponent implements OnInit {


  books: BookList;
  isLoading: boolean;
  cookieExists: boolean = this.cookieService.check('user_name');


  constructor(private activitiesService: ActivitiesService, private cookieService: CookieService) {
  }


  ngOnInit() {
    this.getBooks();
  }

  getBooks() {
    this.isLoading = true;
    this.activitiesService.getUserBooks()
      .pipe(finalize(() => {
        this.isLoading = false;
      }))
      .subscribe((books: BookList) => {
        this.books = books;
      });
  }

  onPageChanged(page: string) {

    this.activitiesService.getUserBooks(page)
      .pipe(finalize(() => {
        this.isLoading = false;
      }))
      .subscribe((books: BookList) => {
        this.books = books;
      });

  }


}
