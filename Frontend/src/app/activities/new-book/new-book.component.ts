import {Component, OnInit} from '@angular/core';
import {NewBookService} from './new-book.service';
import {finalize} from 'rxjs/operators';
import {CookieService} from 'ngx-cookie-service';
import {Router} from '@angular/router';


@Component({
  selector: 'app-new-book',
  templateUrl: './new-book.component.html',
  styleUrls: ['./new-book.component.scss']
})
export class NewBookComponent implements OnInit {


  newBook = {'title': '', 'isbn': ''};
  isLoading: boolean;
  error: string;

  cookieExists: boolean = this.cookieService.check('user_name');


  constructor(private newBookService: NewBookService, private cookieService: CookieService,
              private router: Router) {
  }

  ngOnInit() {
  }

  submit() {
    this.isLoading = true;
    this.newBookService.postNewBook(this.newBook)
      .pipe(finalize(() => {
        this.isLoading = false;
      }))
      .subscribe((r: any) => {
        const result = r;
        this.error = '';
        this.router.navigate(['activities']);

      }, error => this.error = error.error.detail);
  }


}
